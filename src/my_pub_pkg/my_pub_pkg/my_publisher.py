import rclpy

from rclpy.node import Node
from std_msgs.msg import Int64


class NumberPublisherNode(Node):

    def __init__(self):

        super().__init__("number_publisher")

        # Declare Parameters
        self.declare_parameter("number", 2)
        self.declare_parameter("publish_period", 1.0)

        # Get Parameter Values
        self.number_ = self.get_parameter("number").value
        self.publish_period_ = self.get_parameter("publish_period").value

        # Create Publisher
        self.number_publisher_ = self.create_publisher(
            Int64,
            "number",
            10
        )

        # Create Timer
        self.timer_ = self.create_timer(
            self.publish_period_,
            self.publish_number
        )

        self.get_logger().info("Number Publisher Started")

        self.get_logger().info(
            f"Publishing Number: {self.number_}"
        )

        self.get_logger().info(
            f"Publish Period: {self.publish_period_}"
        )

    def publish_number(self):

        msg = Int64()

        msg.data = self.number_

        self.number_publisher_.publish(msg)

        self.get_logger().info(
            f"Publishing: {msg.data}"
        )


def main(args=None):

    rclpy.init(args=args)

    node = NumberPublisherNode()

    rclpy.spin(node)

    rclpy.shutdown()


if __name__ == "__main__":
    main()
