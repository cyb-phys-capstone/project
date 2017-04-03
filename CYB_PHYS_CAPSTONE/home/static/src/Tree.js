

var chart_config = [];

function chartBuilder(nodes, generators, inverters, batteries){
    console.log(nodes[1]);
    console.log(generators[0]);

    chart_config = {
        chart: {
            container: "#custom-colored",

            nodeAlign: "BOTTOM",

            connectors: {
                type: 'step'
            },
            node: {
                HTMLclass: 'nodeExample1'
            }
        },nodeStructure: {
            text: {
                name: "EMS-1",
                title: "ASU-Poly",
                contact: "Server",
            },
            HTMLclass: 'light-gray',
            children: [

            ]

                }
        };
    for (var i =0; i < nodes.length; i++){
        var childOfEMS = { text: {
            name: nodes[i].fields.object_id,
            title: "Node",
            contact: "pi"
            },
            HTMLclass: 'gray',
            children: []
        };

        //Add generator child nodes
        for (var device1 =0; device1 < generators.length; device1++){
            if (generators[i].fields.nc_id == nodes[device1].fields.object_id){
                var generator_node = { text: {
                    name: generators[i].pk,
                    title: generators[i].fields.manufacturer,
                    contact: "Generator"
                    },
                    HTMLclass: 'red'
                };
                childOfEMS.children.push(generator_node);
            }
        }
        //Add battery child nodes
        for (var device2 =0; device2 < batteries.length; device2++){
            if (batteries[i].fields.nc_id == nodes[device2].fields.object_id){
                var battery_node = { text: {
                    name: batteries[i].pk,
                    title: batteries[i].fields.manufacturer,
                    contact: "Battery"
                    },
                    HTMLclass: 'blue'
                };
                childOfEMS.children.push(battery_node);
            }
        }
        //Add inverter child nodes
        for (var device3 =0; device3 < inverters.length; device3++){
            if (inverters[i].fields.nc_id == nodes[device3].fields.object_id){
                var inverter_node = { text: {
                    name: inverters[i].pk,
                    title: inverters[i].fields.manufacturer,
                    contact: "Inverter"
                    },
                    image: "/static/assets/BatteryCharging.png",
                    HTMLclass: 'green'
                };
                childOfEMS.children.push(inverter_node);
            }
        }
        chart_config.nodeStructure.children.push(childOfEMS);
    }

}