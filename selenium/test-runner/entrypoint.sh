#!/bin/sh
TEST_TARGET=$1
TEST_IN_CI=${TEST_IN_CI:false}

if "${TEST_IN_CI}"; then
  echo "アタッチして$TEST_TARGETを実行してください"
  sh
else
  pytest $TEST_TARGET
fi
