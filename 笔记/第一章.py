"""
协议：规定多个用户实体之间应该如何传递信息以及接收/发送信息之后应该进行怎样的操作的规则
分组交换：在交换信息的时候，有的时候因为信息过大发送的时候会将信息分割成一个一个的小块，这样就被称为分组
        分组交换机   路由器/链路层交换机
排队时延：路由器在转发报文段的时候因为内部是有缓存大小的，如果后来的报文遇到前面还没发送完成就要等待一段时间，
        这个时间就是排队时延
分组丢失：路由器的缓存已经满了的时候有新的报文段进入，那么因为内部无法缓存，就会导致报文段的丢失被称为分组丢失(丢包)
五层协议栈：因为七层协议栈不是很实用这本是按照五层协议栈来讲的
    应用层   具体实施的协议例如HTTP这样的
    传输层    TCP UDP
    网络层     IP
    数据链路层   传输数据的链路分组称为帧
    物理层     具体的物理链路例如光纤

"""