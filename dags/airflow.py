from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.decorators import task
from airflow.operators.bash import BashOperator

# A DAG represents a workflow, a collection of tasks
with DAG(dag_id="full_process", start_date=days_ago(1)) as dag:
    # Tasks are represented as operators
    start = BashOperator(task_id="start", bash_command="echo starting")
    # test = BashOperator(task_id="test", bash_command="python /opt/airflow/scripts/formatting/hello.py")
    
    ### Scraping
    scraping_search = BashOperator(task_id="scraping_search", bash_command="python /opt/airflow/scripts/scraping/scopus_search.py")
    scraping_abstract = BashOperator(task_id="scraping_abstract", bash_command="python /opt/airflow/scripts/scraping/abstract_retrieval.py")

    ### Formatting
    formatting = BashOperator(task_id="formatting", bash_command="python /opt/airflow/scripts/formatting/formatter.py")

    ### Visualizing
    visualize = BashOperator(task_id="new-data-is-ready", bash_command='echo "Your latest data is ready! Use Streamlit run to visualize it."')

    # Set dependencies between tasks
    start >> scraping_search
    scraping_search >> scraping_abstract
    scraping_abstract >> formatting
    formatting >> visualize

