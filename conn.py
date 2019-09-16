from ats.topology import loader
tb = loader.load("tb.yaml")

dev = tb.devices['mydev']
dev.connect()
dev.execute("hostname")
dev.disconnect()



