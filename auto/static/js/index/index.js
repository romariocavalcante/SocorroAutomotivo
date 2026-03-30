let map;
        const chicago = { lat: 41.85, lng: -87.65 };
        function createCenterControl(map) {
            const controlButton = document.createElement("button");
            controlButton.classList.add('buttonStyle');
            controlButton.textContent = "Center Map";
            controlButton.title = "Click to recenter the map";
            controlButton.type = "button";
            controlButton.addEventListener("click", () => {
                map.setCenter(chicago);
            });
            return controlButton;
        }

        function initMap() {
            map = new google.maps.Map(document.getElementById("map"), {
                zoom: 4,
                center: { lat: 49.496675, lng: -102.65625 },
            });
            var georssLayer = new google.maps.KmlLayer({
                url: "http://api.flickr.com/services/feeds/geo/?g=322338@N20&lang=en-us&format=feed-georss",
            });
            georssLayer.setMap(map);
            const centerControlDiv = document.createElement("div");
            const centerControl = createCenterControl(map);
            centerControlDiv.appendChild(centerControl);
            map.controls[google.maps.ControlPosition.TOP_CENTER].push(
                centerControlDiv
            );
        }
        window.initMap = initMap;