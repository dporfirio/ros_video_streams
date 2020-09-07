import rclpy
from rclpy.node import Node

from sensor_msgs import Image

class Controller(Node):

	def __init__(self):
		super().__init__('monitor_node')

		self.img_sub1 = self.create_subscription(Image, "/study/feed1", self.feed_callback1, 10)
		self.img_sub2 = self.create_subscription(Image, "/study/feed1", self.feed_callback2, 10)
		self.figaro_feed = self.create_subscription(Image, "/ir/image_raw", self.figaro_feed_callback, 10)

	def feed_callback1(self,msg):
		pass

	def feed_callback2(self,msg):
		pass

	def figaro_feed(self, msg):
		pass

def main():
    rclpy.init()
    controller = Controller()
    rclpy.spin(controller)

if __name__ == '__main__':
    main()
