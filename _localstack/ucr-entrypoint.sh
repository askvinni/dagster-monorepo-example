export SNOWFLAKE_ACCOUNT="aa00000.eu-central-1"
export SNOWFLAKE_WAREHOUSE="my_cool_warehouse"
export SNOWFLAKE_USER="$(cat /run/secrets/snowflake_user)"
export SNOWFLAKE_PASSWORD="$(cat /run/secrets/snowflake_password)"

dagster api grpc -h 0.0.0.0 -p 4266 --package-name $1