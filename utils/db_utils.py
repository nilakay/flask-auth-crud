import psycopg2
import copy
from utils.utils import read_yaml, get_logger, get_error_logger

logger = get_logger()
error_logger = get_error_logger()

def get_db_connection():
    config = read_yaml("/Users/nilakay/Desktop/flask2_checkpoint4_copy/config/db.yaml")
    try:
        conn = psycopg2.connect(
            dbname=config["database"]["dbname"],
            user=config["database"]["user"],
            password=config["database"]["password"],
            host=config["database"]["host"],
            port=config["database"]["port"]
        )
        return conn
    except psycopg2.Error as e:
        error_logger.error(f"Failed to connect to database: {e}")
        raise

def execute_query(base_query, replacements, params=None): 
    try:
        conn = get_db_connection() 
        with conn.cursor() as cur:
            query = copy.deepcopy(base_query)
            for key, value in replacements.items():
                query = query.replace(f"{{{key}}}", value)
            cur.execute(query, params)
            logger.info(f"operation successful on {query} with params {params}")
            if "SELECT" in query:
                return cur.fetchall()
            else:
                conn.commit()
    except Exception as e:
        error_logger.error(f"Failed to execute: {query} with params {params}: {e}")
        raise
    finally:
        conn.close()  
