# flow_node_engine

NodeFlowEngine节点流处理引擎：

设计三类节点分别为：SourceNode(数据源节点)、TransformNode(处理节点)、SinkNode(数据输出节点)

任务的流程：源->处理->输出

每个节点均以线程方式运行，由数据驱动，切换节点的运行状态，数据的流向为父节点->子节点


![img_1](https://user-images.githubusercontent.com/35550265/212549444-13e06a0c-ed7f-4718-8a68-6642bd49c43f.png)
