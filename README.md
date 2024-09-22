# Team_Yodo

# Water and Beach Monitoring

## Overview

This project involves monitoring water and beach conditions using various data sources and machine learning models.
We are developing an app that detects whether people are drowning in open water.

## Tidal Info

We developed a Python script that interacts with tidal and weather APIs, and calculated the level of risk.

### Risks

-   **Wind**: The strength of the wind determines the risk.
-   **Temperature**: Colder temperatures increase the risk.
-   **Tide**: The difference between the tides determines the level of risk.

## Future Work
- Decrease the zone of clarity
- Insert another method that would update the value

## Swimmer Detection

We created a model using YOLOv8n as a base to detect humans and swimmers.

## Future Work

-   Enhance the risk calculation functions.
-   Improve the accuracy of the swimmer detection model.
-   Integrate additional data sources for more comprehensive monitoring.
-   Have zone of clarity

## How to Use

1. Clone the repository.
2. Install the required dependencies.
3. Run the Python script for tidal info.
4. Use the YOLOv8n model for swimmer detection.

## License

This project is licensed under the MIT License.
