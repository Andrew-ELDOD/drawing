import rclpy
from rclpy.node import Node
from std_msgs.msg import String



class shape_node(Node):
    def __init__(self):
        super().__init__("shape_node")
        self.Shape_node_publish = self.create_publisher(String,"chatter",10)
        self.get_logger().info("Shape node activated")
        self.create_timer(1.0,self.from_user)
    

    def from_user(self):
        shape_type=input("enter star , heart , infinity  for drawing :  ")
        msg=String()
        msg.data=shape_type.lower()
        self.Shape_node_publish.publish(msg)
        self.get_logger().info(f"shape node publish {msg.data}")
    
    

def main(args=None):
    rclpy.init(args=args)
    node = shape_node()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()