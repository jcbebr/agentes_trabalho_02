var options = {
                "layout": {
                    "hierarchical": {
                        "direction": "UD",
                    },
                },
                "configure": {
                    "enabled": false
                },
                "edges": {
                    "color": {
                        "inherit": true
                    },
                    "smooth": {
                        "enabled": true,
                        "type": "dynamic"
                    }
                },
                "interaction": {
                    "dragNodes": true,
                    "hideEdgesOnDrag": false,
                    "hideNodesOnDrag": false
                },
                "physics": {
                    "enabled": true,
                    "stabilization": {
                        "enabled": true,
                        "fit": true,
                        "iterations": 1000,
                        "onlyDynamicEdges": false,
                        "updateInterval": 50
                    }
                }
            };