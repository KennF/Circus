require 'bunny'

conn = Bunny.new(:host => "10.148.204.225", :user => "fuke", :password => "changeit")
conn.start

ch = conn.create_channel

q = ch.queue("hello")
ch.default_exchange.publish("Hello World!", :routing_key => q.name)

puts " [x] Sent 'Hello World!'"

ch.close
