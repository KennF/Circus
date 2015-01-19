require 'bunny'

conn = Bunny.new(:host => "10.148.204.225", :user => "fuke", :password => "changeit")
conn.start

ch = conn.create_channel
exchanger = ch.fanout("logs")
# it is a temperory queue, which will be deleted after use.
q = ch.queue("", :persistent => true, :exclusive => true)

q.bind(exchanger)

puts " [*]Waiting for logs, to exit press CTRL+C"

begin 
  q.subscribe(:manual_ack => true, :block => true) do |delivery_info, properties, body|
    puts " [*]#{body}"

    ch.ack(delivery_info.delivery_tag)
  end
rescue Interrupt => _
  ch.close
  conn.close
end

