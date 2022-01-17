from typing import Dict, List, Text

from pyflink.table.sql_dialect import SqlDialect

from ai_flow.util.json_utils import Jsonable
from ai_flow_plugins.job_plugins import flink as flink_plugin
from pyflink.table import Table
from pyflink.table.catalog import HiveCatalog


HIVE_USER_FEATURE_GEN_CONFIG_KEY = "gen_config"

class HiveUserFeatureGenerator(flink_plugin.FlinkPythonProcessor):
    def process(self,
                execution_context: flink_plugin.ExecutionContext,
                input_list: List[Table] = None,
        ) -> List[Table]:
        """
        Generate two random user feature tables into hive
        """
        gen_config:Dict = execution_context.config[HIVE_USER_FEATURE_GEN_CONFIG_KEY]
        hive_catalog_name = gen_config['catalog_name']
        hive_database = gen_config['default_database']
        hive_conf_dir = gen_config['hive_conf_dir']
        user_num = int(gen_config['user_num'])

        t_env = execution_context.table_env
        s_set = execution_context.statement_set

        # setup catalog
        hive_catalog = HiveCatalog(hive_catalog_name, hive_database, hive_conf_dir)
        t_env.register_catalog(hive_catalog_name, hive_catalog)
        t_env.use_catalog(hive_catalog_name)

        # Create source tables with Flink datagen connector
        t_env.execute_sql(f"""
        CREATE TEMPORARY TABLE TEMP_USER_FEATURE_A (
        user_id BIGINT,
        a FLOAT
        ) WITH (
        'connector' = 'datagen',
        'number-of-rows' = 10000,

        'fields.user_id.kind'='sequence',
        'fields.user_id.start'='1',
        'fields.user_id.end'='{user_num}',

        'fields.a.min'='0',
        'fields.a.max'='1'
        )
        """)

        t_env.execute_sql(f"""
        CREATE TEMPORARY TABLE TEMP_USER_FEATURE_B (
        user_id BIGINT,
        b1 FLOAT,
        b2 FLOAT
        ) WITH (
        'connector' = 'datagen',
        'rows-per-second' = '10000', 

        'fields.user_id.kind' = 'sequence',
        'fields.user_id.start' = '1',
        'fields.user_id.end' = '{user_num}',

        'fields.b1.min' = '0',
        'fields.b1.max' = '1',
        'fields.b2.min' = '0',
        'fields.b2.max' = '1'
        )
        """)

        t_env.get_config().set_sql_dialect(SqlDialect.HIVE)
        t_env.execute_sql(f"""
        CREATE TABLE IF NOT EXISTS USER_FEATURE_A  (
        user_id BIGINT,
        a FLOAT
        )
        """)
        t_env.execute_sql(f"""
        CREATE TABLE IF NOT EXISTS USER_FEATURE_B (
        user_id BIGINT,
        b1 FLOAT,
        b2 FLOAT
        )
        """)

        t_env.get_config().set_sql_dialect(SqlDialect.DEFAULT)

        # use statement set to execute sql together to fix current flink-ai-flow implementation
        s_set.add_insert_sql(f"""
        INSERT OVERWRITE USER_FEATURE_A
        SELECT user_id, a
        FROM TEMP_USER_FEATURE_A
        """)

        s_set.add_insert_sql(f"""
        INSERT OVERWRITE USER_FEATURE_B
        SELECT user_id, b1, b2
        FROM TEMP_USER_FEATURE_B
        """)

        return []
