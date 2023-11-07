# knowledge-graph
## Step 1. Install Neo4j docker
```=
docker run \
    --name neo4j \
    -p7474:7474 -p7687:7687 \
    -d \
    -v /var/neo4j/data:/data \
    -v /var/neo4j/logs:/logs \
    -v /var/neo4j/import:/var/lib/neo4j/import \
    -v /var/neo4j/plugins:/plugins \
    --env NEO4J_AUTH=neo4j/password \
    neo4j:latest
```
## Step 2. Create flask project
## Step 3. Install requirements.txt
## Step 4. Replace index.html & app.py File
## Step 5. Upload CSV File
```=
csv File is in the dataset folder
備註：
1. 有分上傳 Node 跟 Relation 兩者地方不同
   => entity_list.csv 是上傳 Nodes
   => relation_data.csv 是上傳 Relations
2. panda 繪圖比較慢，上傳後需要等一下重新整理後再等一下就會出現
```
### 上傳 CSV 的地方
![image](https://github.com/YiJunKo/neo4j-knowledge-graph/assets/50664144/aade4ebb-5616-4e08-8dff-2d64a9b637fa)

### 成品畫面
![image](https://github.com/YiJunKo/neo4j-knowledge-graph/assets/50664144/2bb6c56b-383f-4b62-899a-841e75c826b5)

