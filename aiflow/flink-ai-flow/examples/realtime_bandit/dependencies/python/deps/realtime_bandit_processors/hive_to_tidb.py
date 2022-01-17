from typing import Dict, List, Text, Tuple

from pyflink.table.sql_dialect import SqlDialect

from ai_flow.util.json_utils import Jsonable
from ai_flow_plugins.job_plugins import flink as flink_plugin
from pyflink.table import Table
from pyflink.table.catalog import HiveCatalog

import mysql.connector


class HiveToTidbTableEnv(flink_plugin.FlinkStreamEnv):
    def create_env(self):
        exec_env, t_env, s_set = super().create_env()
        t_env.get_config().get_configuration().set_boolean(
            "table.exec.hive.infer-source-parallelism", False)
        t_env.get_config().get_configuration().set_integer(
            "table.exec.hive.infer-source-parallelism.max", 1)
        return exec_env, t_env, s_set

class UserFeatureHiveToTidb(flink_plugin.FlinkPythonProcessor):
    def process(self,
                execution_context: flink_plugin.ExecutionContext,
                input_list: List[Table] = None,
                ) -> List[Table]:
        """
        Generate two random user feature tables into hive
        """
        conf: Dict = execution_context.config['conf']
        hive_catalog_name = conf['catalog_name']
        hive_database = conf['default_database']
        hive_conf_dir = conf['hive_conf_dir']

        db_url = conf['db_url']
        db_host = conf['db_host']
        db_port = int(conf['db_port'])
        db_database = conf['db_database']
        db_username = conf['db_username']
        db_password = conf['db_password']
        db_table_name = conf['db_table_name']

        t_env = execution_context.table_env
        s_set = execution_context.statement_set

        # setup catalog
        hive_catalog = HiveCatalog(
            hive_catalog_name, hive_database, hive_conf_dir)
        t_env.register_catalog(hive_catalog_name, hive_catalog)
        t_env.use_catalog(hive_catalog_name)

        # create table in tidb
        db_conn = mysql.connector.connect(
            host=db_host,
            port=db_port,
            user=db_username,
            password=db_password,
            database=db_database,
        )
        db_cursor = db_conn.cursor()
        db_cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {db_table_name} (
        user_id BIGINT,
        a FLOAT,
        b1 FLOAT,
        b2 FLOAT,
        PRIMARY KEY (user_id)
        )
        """)
        
        t_env.execute_sql(f"""
        CREATE TABLE IF NOT EXISTS {db_table_name} (
        user_id BIGINT,
        a FLOAT,
        b1 FLOAT,
        b2 FLOAT,
        PRIMARY KEY (user_id) NOT ENFORCED
        ) WITH (
        'connector' = 'tidb',
        'tidb.database.url' = 'jdbc:{db_url}',
        'tidb.username'   = '{db_username}',
        'tidb.password'   = '{db_password}',
        'tidb.table.name' = 'TIDB_USER_FEATURES',
        'tidb.write_mode' = 'upsert'
        )
        """)

        # Create source tables with Flink datagen connector
        source_table = t_env.sql_query(f"""
        SELECT USER_FEATURE_A.user_id, a, b1, b2
        FROM USER_FEATURE_A INNER JOIN USER_FEATURE_B on USER_FEATURE_A.user_id = USER_FEATURE_B.user_id
        """)

        s_set.add_insert(db_table_name, source_table)

        return []
