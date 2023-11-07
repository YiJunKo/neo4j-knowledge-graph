from flask import Flask, render_template, jsonify, request
from py2neo import Graph, Node, Relationship
import pandas as pd

# 連上neo4j community
# windows
# 終端機輸入
# cd C:\neo4j-community-5.11.0\bin
# neo4j console
# 啟動 neo4j 數據庫
# 終端機按下
# control + C
# 關閉neo4j 數據庫
url = "neo4j://localhost:7687"
username = "neo4j"
password = "password"
graph = Graph(url, auth=(username, password))

# 清空 neo4j 數據庫
graph.delete_all()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/uploadNodes', methods=['POST'])
def upload_csv1():
    try:
        csv_file = request.files['csvFile']
        if csv_file:
            # 保存上传的CSV文件
            csv_file.save('/var/neo4j/import/' + csv_file.filename)

            # 读取CSV文件并将数据导入Neo4j
            df = pd.read_csv('/var/neo4j/import/' + csv_file.filename)
            for _, row in df.iterrows():
                node = Node(row["type"], Name=row["entity_name"], Type=row["type"])
                graph.create(node)
                # 在此处编写将数据插入Neo4j的代码
                # 例如，可以使用Cypher语句将数据插入到数据库
                pass  # 用于占位，表示这里需要添加代码

            return jsonify({'message': 'CSV file uploaded and data imported to Neo4j successfully.'})

        return jsonify({'message': 'No file uploaded.'})

    except Exception as e:
        return jsonify({'message': str(e)})


@app.route('/uploadRelations', methods=['POST'])
def upload_csv2():
    try:
        csv_file = request.files['csvFile']
        if csv_file:
            # 保存上传的CSV文件
            csv_file.save('/var/neo4j/import/' + csv_file.filename)

            # 读取CSV文件并将数据导入Neo4j
            df = pd.read_csv('/var/neo4j/import/' + csv_file.filename)
            for _, row in df.iterrows():
                starting_node = graph.nodes.match(Name=row["head"]).first()
                ending_node = graph.nodes.match(Name=row["tail"]).first()
                # print(starting_node)
                # print(ending_node)
                relationship = Relationship(starting_node, row["relation"], ending_node)
                graph.create(relationship)
                # 在此处编写将数据插入Neo4j的代码
                # 例如，可以使用Cypher语句将数据插入到数据库
                pass  # 用于占位，表示这里需要添加代码

            return jsonify({'message': 'CSV file uploaded and data imported to Neo4j successfully.'})

        return jsonify({'message': 'No file uploaded.'})

    except Exception as e:
        return jsonify({'message': str(e)})


if __name__ == '__main__':
    app.run(debug=True)