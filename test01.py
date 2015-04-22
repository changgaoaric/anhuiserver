import httplib
def check_web_server(host,port,path):
	h = httplib.HTTPConnect(host,port)
	h.request('GET',path)
	resp=h.getresponse()
	print "HTTP Response:"
	print "status = ",resp.status
	print "reason = ",resp.reason
	print "HTTP hEARDER:"
	for hdr in resp.getheaders():
		print '%s:%s' % hdr
