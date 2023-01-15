# flow_node_engine

NodeFlowEngine节点流处理引擎：

设计三类节点分别为：SourceNode(数据源节点)、TransformNode(处理节点)、SinkNode(数据输出节点)

任务的流程：源->处理->输出

每个节点均以线程方式运行，由数据驱动，切换节点的运行状态，数据的流向为父节点->子节点


![Image](https://github.com/windyboyj/flow_node/blob/main/blob-image/img_1.png)

