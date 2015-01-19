require 'bunny'

if ARGV.empty?
  abort "Usage: #{$0} [info] [warning] [error]"
end

conn = Bunny.new(:host => "10.148.204.225", :user => "fuke", :password => "changeit")
conn.start

ch = conn.create_channel
exchanger = ch.direct("direct_logs")
# it is a temperory queue, which will be deleted after use.
q = ch.queue("", :persistent => true, :exclusive => true)

ARGV.each do |severity|
  q.bind(exchanger, :routing_key => severity)
end

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

