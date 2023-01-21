仅限用于学习交流

# flow_node_engine

NodeFlowEngine节点流处理引擎：

设计三类节点分别为：SourceNode(数据源节点)、TransformNode(处理节点)、SinkNode(数据输出节点)

任务的主流程：源->处理->输出

SourceNode：     负责接入不同类型的数据

TransformNode：  负责对数据进行处理

SinkNode：       负责将处理后的数据进行输出，比如打印，视频存储，结果上传等

每个节点均以线程方式运行，由数据驱动，切换节点的运行状态，数据的流向为父节点->子节点，各节点以松耦合的方式运行

同时提出组件的概念，每个节点均包含组件对象，即为节点的具体功能实现，以动态的方式加载组件;

设计观察者模式，定义Subject,Observer, 由子节点向父节点进行注册，当父节点有数据更新时，notify 所有子节点进行数据 update，并且利用小颗粒同步锁，保持数据更新的一致性; 

![img_1](https://user-images.githubusercontent.com/35550265/212549444-13e06a0c-ed7f-4718-8a68-6642bd49c43f.png)


样例程序入口main.py 

任务配置结构体task.json 分为source transforms sinks三部分








