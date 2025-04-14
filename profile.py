import geni.portal as portal
import geni.rspec.pg as pg

pc = portal.Context()
request = pc.makeRequestRSpec()

pc.defineParameter(
    "phystype", "Optional physical node type", portal.ParameterType.NODETYPE, ""
)

params = pc.bindParameters()

if params.phystype != "":
    if len(params.phystype.split(",")) != 1:
        pc.reportError(
            portal.ParameterError("Only a single type is allowed", ["phystype"])
        )

pc.verifyParameters()

node = request.RawPC("node")
if params.phystype != "":
    node.hardware_type = params.phystype
node.addService(
    pg.Execute(shell="sh", command="sudo /local/repository/pash/scripts/distro-deps.sh")
)
node.addService(
    pg.Execute(
        shell="sh", command="yes | sudo /local/repository/pash/scripts/setup-pash.sh"
    )
)

pc.printRequestRSpec(request)
