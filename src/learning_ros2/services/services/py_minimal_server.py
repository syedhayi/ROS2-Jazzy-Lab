#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from rclpy.logging import get_logger
from ros2_interfaces.srv import Greetings

class Greeting_server_node_class(Node):
    def __init__(self) -> None:
        super().__init__("Greeting_server")
        self.get_logger().info(f"{self.get_name()} has been started!")
        self.service_ = self.create_service(Greetings, "greetings", self.greetings_callback)

    def greetings_callback(self, request: Greetings.Request, response: Greetings.Response):
        self.get_logger().info(f'Incoming request: "{request.greetings}"')
        response.response_greetings = f'Hello from {self.get_name()}'
        self.get_logger().info(f'Sending response: "{response.response_greetings}"')
        
        return response
    
def main(args=None) -> None:
    log = get_logger("System")
    node_instance = None

    try:
        log.info("Initializing the ROS2 Client...")
        rclpy.init(args=args)

        log.info("Starting a ROS2 Node...")
        node_instance = Greeting_server_node_class()
        rclpy.spin(node_instance)

    except KeyboardInterrupt:
        log.warn("[CTRL+C]>>> Interrupted by the User.")

    except Exception as e:
        log.error(f"Critical Error: {e}")
    
    finally:
        if node_instance is not None:
            log.info("Destroying the ROS2 Node...")
            node_instance.destroy_node()
            node_instance = None

        if rclpy.ok():
            log.info("Manually shutting down the ROS2 Client...")
            rclpy.shutdown()

if __name__ == '__main__':
    main()