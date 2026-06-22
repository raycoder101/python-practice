import sys
from pyflink.common.typeinfo import Types
from pyflink.datastream import StreamExecutionEnvironment

def flink_word_processor():
    # 1. Initialize the Stream Execution Environment
    env = StreamExecutionEnvironment.get_execution_environment()
    
    # Set parallelism to 1 for clean local execution outputs
    env.set_parallelism(1)

    # 2. Define the Stream Data Source (Simulating a real-time stream using a list)
    data_source = ["apple", "banana", "cherry", "apricot", "blueberry"]
    data_stream = env.from_collection(collection=data_source)

    # 3. Apply Transformations 
    # Filter words that start with 'a' and transform them to uppercase
    processed_stream = data_stream \
        .filter(lambda word: word.startswith('a')) \
        .map(lambda word: (word.upper(), len(word)), output_type=Types.TUPLE([Types.STRING(), Types.INT()]))

    # 4. Define the Data Sink (Print the processing output directly to stdout)
    processed_stream.print()

    # 5. Trigger the Flink Application Execution
    print("Submitting and executing the PyFlink streaming job...")
    env.execute("PyFlink Word Processor Job")

if __name__ == '__main__':
    flink_word_processor()
