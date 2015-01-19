require 'bunny'

conn = Bunny.new(:host => "10.148.204.225", :user => "fuke", :password => "changeit")
conn.start

ch = conn.create_channel
exchanger = ch.topic("topic_logs")

severity = ARGV.shift || "anonymous.info"
msg = ARGV.empty? ? "hello world" : ARGV.join(" ")

exchanger.publish(msg, :routing_key => severity)
puts " [x] Sent #{msg}"

conn.close

