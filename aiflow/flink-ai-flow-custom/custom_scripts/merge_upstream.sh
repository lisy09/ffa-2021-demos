#!/usr/bin/env bash

readonly CUSTOM_SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
readonly CUSTOM_DIR="$( cd $CUSTOM_SCRIPT_DIR/.. >/dev/null 2>&1 && pwd )"
readonly ROOT_DIR="$( cd $CUSTOM_DIR/.. >/dev/null 2>&1 && pwd )"
source $CUSTOM_SCRIPT_DIR/.env

readonly CLONE_ROOT_DIR=$ROOT_DIR/$TEMP_CLONE_ROOT_DIR
readonly MERGE_TARGET_DIR=$ROOT_DIR/$MERGE_DIR

mkdir -p $MERGE_TARGET_DIR
rm -rf $MERGE_TARGET_DIR/{..?*,.[!.]*,*}

echo "Copying upstream from $CLONE_ROOT_DIR to $MERGE_TARGET_DIR ..."
cp -r $CLONE_ROOT_DIR/{.[!.]*,*} $MERGE_TARGET_DIR/
rm -rf $MERGE_TARGET_DIR/.git

echo "Merging readme ..."
$CUSTOM_SCRIPT_DIR/merge_readme.sh
echo "Merging readme ... Finished!"

echo "Merging dotenv ..."
$CUSTOM_SCRIPT_DIR/merge_dotenv.sh
echo "Merging dotenv ... Finished!"

echo "Merging makefile ..."
$CUSTOM_SCRIPT_DIR/merge_makefile.sh
echo "Merging makefile ... Finished!"

echo "Merging python requirements ..."
# $CUSTOM_SCRIPT_DIR/merge_python_requirements.sh
echo "Merging python requirements ... Finished!"

echo "Merging scripts ..."
$CUSTOM_SCRIPT_DIR/merge_scripts.sh
echo "Merging scripts ... Finished!"

echo "Merging docker modules ..."
$CUSTOM_SCRIPT_DIR/merge_docker.sh
echo "Merging docker modules ... Finished!"

echo "Merging .vscode/ ..."
$CUSTOM_SCRIPT_DIR/merge_dotvscode.sh
echo "Merging .vscode/ ... Finished!"

echo "Merging pom.xml ..."
$CUSTOM_SCRIPT_DIR/merge_pom.sh
echo "Merging pom.xml!"

echo "Merging custom implementations ..."
# $CUSTOM_SCRIPT_DIR/merge_flink_1_14.sh
$CUSTOM_SCRIPT_DIR/merge_examples.sh
echo "Merging custom implementations!"