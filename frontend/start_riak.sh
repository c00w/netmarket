cd ../../riak/
make devrel
dev/dev1/bin/riak start
dev/dev2/bin/riak start
dev/dev3/bin/riak start
dev/dev4/bin/riak start

dev/dev2/bin/riak-admin join dev1@127.0.0.1
dev/dev3/bin/riak-admin join dev1@127.0.0.1
dev/dev4/bin/riak-admin join dev1@127.0.0.1
