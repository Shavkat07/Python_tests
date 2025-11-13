from abc import ABC, abstractmethod


class PaymentProcessor(ABC):
	@abstractmethod
	def process(self, amount):
		pass


class PayPalProcessor(PaymentProcessor):
	def process(self, amount):
		print(f"PayPalProcessor.process(self, {amount})")


class CardProcessor(PaymentProcessor):
	def process(self, amount):
		print(f"CardProcessor.process(self, {amount})")


class CryptoProcessor(PaymentProcessor):
	def process(self, amount):
		print(f"CryptoProcessor.process(self, {amount})")


paypal = PayPalProcessor()
paypal.process(412)

card = CardProcessor()
card.process(445)

crypto = CryptoProcessor()
crypto.process(122)


# ------------------------------------------------------------------------------------------------------


class MediaFile(ABC):
	@abstractmethod
	def play(self):
		pass



class MP3File(MediaFile):
	def play(self):
		print("MP3 File is playing")

class MP4File(MediaFile):
	def play(self):
		print("MP4 File is playing")

class WavFile(MediaFile):
	def play(self):
		print("Wav File is playing")


a, b, c = MP3File(), MP4File(), WavFile()
for i in a, b, c:
	i.play()
	

# ------------------------------------------------------------------------------------------------------


class Notification(ABC):

	@abstractmethod
	def send(self, address):
		pass


class EmailNotification(Notification):

	def send(self, address):
		print(f"Email Notification has been sent to your email address: {address}")



class SmsNotification(Notification):
	def send(self, address):
		print(f"Sms Notification has been sent to your phone number: {address}")

class PushNotification(Notification):
	def send(self, address):
		print(f"Push Notification has been sent to your browser: {address}")



a, b, c = EmailNotification(), SmsNotification(), PushNotification()
a.send("shavkatkurbanov065@gmail.com")
b.send("+994112912")
c.send("FireFox:19119453")

# ------------------------------------------------------------------------------------------------------
