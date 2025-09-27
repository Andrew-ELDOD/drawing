import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist 
from std_msgs.msg import String
import time
from math import pi

class Commander(Node):
    def __init__ (self):
        super().__init__("turtle_commander")
        self.subscripe_node=self.create_subscription(String,"chatter",self.call_back,10)
        self.publisher_turtle=self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.get_logger().info("turtle commander activated")
        
        

    def call_back(self,msg:String):
        
        shape = msg.data
        self.get_logger().info(f"subscripped {shape}")
        if shape == "star":
            self.draw_star()
        elif shape == "heart":
            self.draw_heart()  
        elif shape=="infinity":
            self.draw_infinity()      
            
    
    def draw_star(self):
        msg=Twist()
        for i in range(5):
            msg.linear.x = 2.0
            msg.angular.z = 0.0
            self.publisher_turtle.publish(msg)
            time.sleep(1.2)
            msg.linear.x = 0.0
            msg.angular.z =2.513  
            self.publisher_turtle.publish(msg)
            time.sleep(1.2)
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        self.publisher_turtle.publish(msg)
    
    def draw_heart(self):
        msg = Twist()
        for i in range(4):
            msg.linear.y =  1.5
            msg.angular.z = 1.0
            self.publisher_turtle.publish(msg)
            time.sleep(1)
        for i in range(6):
            msg.linear.y =  0.6
            msg.angular.z = 0.0
            self.publisher_turtle.publish(msg)
            time.sleep(1)
        
        msg.linear.y =  0.0
        msg.angular.z = -pi/2
        self.publisher_turtle.publish(msg)
        time.sleep(1)
        for i in range(6):    
            msg.linear.y = -0.6
            msg.angular.z = 0.0
            self.publisher_turtle.publish(msg)    
            time.sleep(1)  
        
        msg.linear.y =  0.0
        msg.angular.z =pi
        self.publisher_turtle.publish(msg)   
        time.sleep(1)  
        for i in range(4):
            msg.linear.y =  1.5
            msg.angular.z = 1.0
            self.publisher_turtle.publish(msg)
            time.sleep(1)
        msg.linear.y= 0.0
        msg.angular.z=-pi
        self.publisher_turtle.publish(msg)
    
    def draw_infinity(self):
        msg =Twist()
        msg.linear.x = 2.0
        msg.angular.z = 4.0
        self.publisher_turtle.publish(msg)
        time.sleep(1.2)
        
        msg.linear.x = 2.0
        msg.angular.z = 0.0
        self.publisher_turtle.publish(msg)
        time.sleep(1.5)

        msg.linear.x = 2.0
        msg.angular.z = -4.0
        self.publisher_turtle.publish(msg)
        time.sleep(1.2)
        
        msg.linear.x = 2.0
        msg.angular.z = 0.0
        self.publisher_turtle.publish(msg)
        time.sleep(1.5)

        msg.linear.x = 0.0
        msg.angular.z = 0.0
        self.publisher_turtle.publish(msg)
        



def main(args=None):
    rclpy.init(args=args)
    node=Commander()
    rclpy.spin(node)
    
    rclpy.shutdown()

if __name__ == "__main__":
    main()