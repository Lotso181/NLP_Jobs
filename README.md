## 自然语言处理课程作业


[本次实验内容]

1. 使用云服务器部署chatglm2-6b，并设计Prompt，完成选题任务：给定一段文本，以及指定的实体（任五、地点、机构等），抽取与该实体相关的Key-Value知识。

2. 基本要求（每一个⭐️=10分）：

1.[Remote LLM 测试 ⭐️⭐️]      自己准备不少于3个例子，在远程大模型上测试。
2.[Local LLM 测试效果  ⭐️⭐️]   自己准备不少于3个例子（保持同上），在本地大模型上测试。
3.[Local LLM 部署情况 ⭐️]      检查是否已经在本地部署了大模型
4.[Local LLM 应用开发 ⭐⭐️⭐️]    是否已经将所选定的大模型、任务封装成了一个可以直接调用的代码（实现批量输入、批量输出、错误异常管理等，需要自己准备大量测试数据）
5.[文档⭐️⭐️]                  本次作业每个小组都必须以Github/Gitlab项目的方式提交，其中的Readme.md 为本次实验报告的文档。

[模型试验用例]

CN：
1. 我将给定一段文本，以及指定的实体中国，你来抽取与该实体相关的Key-Value知识。以下是文本：中国是一个伟大的国家，5000多年的风雨沧桑孕育出了伟大奋斗、伟大创造、伟大担当、伟大力量等等这些熔铸于民族血脉的伟大基因，烙印于人民心底的伟大精神。

2. 我将给定一段文本，以及指定的实体大语言模型，你来抽取与该实体相关的Key-Value知识。以下是文本：大型语言模型是一种应用深度学习技术并在大量文本数据上训练的人工智能系统。它因其理解和生成人类语言的能力而闻名，这使其能够执行多种自然语言处理任务，例如语言生成、填充、总结、翻译和问答。

3. 我将给定一段文本，以及指定的实体自然语言处理，你来抽取与该实体相关的Key-Value知识。以下是文本：自然语言处理，是计算机科学和信息检索这些跨学科子领域的一个部分。它主要关注如何赋予计算机支持和处理人类语言的能力。NLP合并了计算语言学（人类语言的基于规则的建模）与统计学和机器模型，以此实现计算机理解、生成和操纵人类语言的目标。

EN:
1. Given a text passage and the specified entity 'China,' I will extract Key-Value knowledge pertinent to the entity. The text is as follows: China is a great nation, over 5000 years of historic vicissitudes have fostered great traits of struggle, creation, responsibility, and power ingrained in the nation's bloodline, forming a grand spirit imprinted in the people's hearts.

2. Provided with a text passage and the specified entity 'large language model,' I will derive Key-Value knowledge associated with the entity. Below is the text: Large language models represent artificial intelligence systems developed through deep learning techniques and trained on extensive text datasets. Known for their capacity to comprehend and generate human language, they are capable of performing various natural language processing tasks such as language generation, completion, summarization, translation, and question-answering.

3. Upon receiving a text and the specified entity 'natural language processing,' I will extract related Key-Value knowledge concerning the entity. Here is the text: Natural language processing is a subsection of interdisciplinary fields within computer science and information retrieval. Its primary focus is on enabling computers to support and manipulate human language. NLP integrates computational linguistics, which is the rule-based modeling of human language, with statistics and machine models, aiming to achieve the computer's understanding, generation, and manipulation of human language.

[部署说明]

本次实验项目在autodl算力云服务器(https://www.autodl.com)实现。
![image](https://github.com/Lotso181/NLP_Jobs/assets/117101606/9c99ec95-2a0e-499a-ba4a-8b295fe67c40)


[部署步骤]

1. 创建实例，并打开终端，输入```source /etc/network_turbo```，实现autodl官方的学术加速，以便后续从huggface官方仓库克隆项目。

2. 在终端中，安装git lfs
```
   # 先安装Git（如果尚未安装）
   sudo apt-get install git
   # 安装Git LFS
   curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
   sudo apt-get install git-lfs
   # 设置Git LFS
   git lfs install
```
Git LFS（Large File Storage）是一款开源的 Git 扩展工具，旨在改善大型文件的处理方式，使得用户可以更有效地版本控制这些文件。

在终端切换到autpdl-tmp,创建文件夹chatglm2-6b用以存放模型文件，使用
```
    git clone https://huggingface.co/THUDM/chatglm2-6b
```
下载模型。
接下来创建cahtglm2-6b-code文件夹，来存放代码。并切换到该目录下执行
```
    git clone https://github.com/THUDM/ChatGLM-6B.git
```
下载完成后进入chatglm2-6b-code目录,接下来下载chatglm2代码运行所需要的相关依赖，执行以下命令即可下载：
```
    pip install -r requirements.txt
```

3. 开始运行程序，打开cli_demo.py将模型路径改为我们刚刚保存的路径```/root/autodl-tmp/chatglm2-6b```。将文件保存后，在终端输入
```
python cli_demo.py
```
运行命令行demo。
输出为：
```
 欢迎使用 ChatGLM2-6B 模型，输入内容即可进行对话，clear 清空对话历史，stop 终止程序

    用户：你好

    ChatGLM-6B：你好👋！我是人工智能助手 ChatGLM2-6B，很高兴见到你，欢迎问我任何问题。

    用户：晚上睡不着应该怎么办

    ChatGLM-6B：抱歉，作为一个人工智能助手，我没有能力判断你的睡眠质量。但是，关于睡眠问题，我可以给你一些建议。

    1. 晚上在睡觉前 2-3 小时避免喝咖啡、茶和碳酸饮料，因为这些饮料中含有的咖啡因会让大脑更加兴奋，难以入睡。
    2. 睡前避免使用电子设备，如手机、电脑等。这些设备会发出蓝光，会影响睡眠质量。
    3. 改变睡眠环境，保持舒适的温度，以帮助更容易入睡。
    4. 尝试放松技巧，如深呼吸、瑜伽或冥想，缓解压力和焦虑，有助于入睡。
    5. 如果躺在床上 20 分钟后仍然无法入睡，不要继续躺在床上，而是起床做些轻松的活动，如读书或听轻柔的音乐，直到感到困倦再返回床上。

    如果你有严重的睡眠问题，建议咨询医生或专业的医学机构进行诊断和治疗。
```
至此，基本的chatglm2-6b部署完成。

[注意事项]

1. 在本次实验中，需要使用到openai的格式进行api部署，所以需要运行openai_api.py而不是运行api.py。

2. 此外，autodl云服务器由于实例无独立公网IP，因此不能任意开启额外的端口。启动成功后的访问地址是个本地内网地址，我们无法访问，此时可以通过配置反向SSH来访问该地址,输入:
```
ssh -CNg -L 6006:127.0.0.1:6006  root@connect.westc.gpuhub.com -p 11131
```
![image](https://github.com/Lotso181/NLP_Jobs/assets/117101606/fc75dd47-2f5f-4ee4-9f38-80d476c2f2e4)


其中```6006:127.0.0.1:6006```表示从云服务器上的6006端口映射到本地的6006端口。```root@connect.westc.gpuhub.com -p 11131```在autodl进行获取：

![image](https://github.com/Lotso181/NLP_Jobs/assets/117101606/ee49f548-1e53-4dd6-b669-795d0042daee)


实验结果：

![image](https://github.com/Lotso181/NLP_Jobs/assets/117101606/d1d8416c-8797-45cf-85fc-72fbc99b0e60)

