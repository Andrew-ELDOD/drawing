from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    id = LaunchDescription()
    
    
    first_node =Node(
        package='turtle',
        executable='ShapeNode',
        name='shape_node'
        )
    second_node =Node(
        package='turtle',
        executable='turtle_Commander',
        name='turtle_commander'
        )
    turtlesim= Node(
        package='turtlesim',
        executable='turtlesim_node',
        name='turtlesim'
    )
    
    id.add_action(first_node)
    id.add_action(second_node)
    id.add_action(turtlesim)
    
    return id
