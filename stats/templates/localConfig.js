{
  graphitePort: 2003
, graphiteHost: "{{ inventory_hostname }}"
, port: 8125
, backends: [ "./backends/graphite" ]
, graphite: {
	legacyNamespace: false
  }
}