from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    use_sim_time = LaunchConfiguration("use_sim_time")

    return LaunchDescription([
        DeclareLaunchArgument(
            "use_sim_time",
            default_value="false",
        ),

        Node(
            package="clustering_segmentation",
            executable="clustering_segmentation",
            name="mapping_and_clustering_node",
            output="screen",
            parameters=[
                {"use_sim_time": use_sim_time},
                {"clustering": True},
                {"DynamicStatic_clusters_segmentation": True},
                {"static_mapping": True},
                {"static_points_topic": "static/laserscan"},
                {"clustering_points_topic_in": "filtered/ls/pointcloud"},
                {"clustering_points_topic_out": "clustered_points"},
                {"PrintTimeMetric": False},
                {"SaveTimeMetric": False},
                {"threshold_occupancy": 0.65},
                {"occupancy_percentage": 0.12},
            ],
        ),
    ])
