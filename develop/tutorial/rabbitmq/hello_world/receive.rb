require 'bunny'

conn = Bunny.new(:host => "10.148.204.225", :user => "fuke", :password => "changeit")
conn.start

ch = conn.create_channel
q = ch.queue("hello")

puts " [*] Waiting for messages in #{q.name}, To exit press CTRL+C"

q.subscribe(:block => true) do |delivery_info, properties, body|
  puts " [x] Received #{body}"

  delivery_info.consumer.cancel
end
