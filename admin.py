from kafka import KafkaAdminClient
from kafka.admin import NewPartitions

topic = 'topic_test'
bootstrap_servers = 'localhost:9092'

admin_client = KafkaAdminClient(bootstrap_servers=bootstrap_servers)
topic_partitions = {}
topic_partitions[topic] = NewPartitions(total_count=3)
admin_client.create_partitions(topic_partitions)