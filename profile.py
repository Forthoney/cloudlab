import geni.portal as portal
import geni.rspec.pg as pg

pc = portal.Context()
request = pc.makeRequestRSpec()

node = request.RawPC("node")
node.hardware_type = "r320"
node.addService(pg.Execute(shell="sh", command="/local/repository/setup.sh"))

pc.printRequestRSpec(request)
