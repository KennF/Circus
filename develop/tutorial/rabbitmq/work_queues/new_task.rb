require 'bunny'

conn = Bunny.new(:host => "10.148.204.225", :user => "fuke", :password => "changeit")
conn.start

ch = conn.create_channel
# durable queue
q = ch.queue("task_queue", :durable => true)

msg  = ARGV.empty? ? "Hello World!" : ARGV.join(" ")

# publish the message and ask server to make it persistent
q.publish(msg, :persistent => true)
puts " [x] Sent #{msg}"

sleep 1
ch.close
