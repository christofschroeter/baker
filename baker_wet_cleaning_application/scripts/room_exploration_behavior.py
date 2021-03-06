#!/usr/bin/env python

import rospy
import actionlib

from ipa_building_msgs.msg import *

import behavior_container

class RoomExplorationBehavior(behavior_container.BehaviorContainer):

	def __init__(self, interrupt_var_, service_str_):
		self.interrupt_var = interrupt_var_
		self.service_str = service_str_

	# Method for returning to the standard pose of the robot
	def returnToRobotStandardState(self):
		# save current data if necessary
		# undo or check whether everything has been undone
		pass

	# Method for setting parameters for the behavior
	def setParameters(self, map_data, input_map, map_resolution, map_origin, robot_radius, coverage_radius, field_of_view, starting_position, planning_mode):
		self.map_data_ = map_data
		self.input_map_ = input_map
		self.map_resolution_ = map_resolution
		self.map_origin_ = map_origin
		self.robot_radius_ = robot_radius
		self.coverage_radius_ = coverage_radius
		self.field_of_view_ = field_of_view
		self.starting_position_ = starting_position
		self.planning_mode_ = planning_mode

	# Implemented Behavior
	def executeCustomBehavior(self):
		exploration_goal = RoomExplorationGoal()
		exploration_goal.input_map = self.input_map_
		exploration_goal.map_resolution = self.map_resolution_
		exploration_goal.map_origin = self.map_origin_
		exploration_goal.robot_radius = self.robot_radius_
		exploration_goal.coverage_radius = self.coverage_radius_
		exploration_goal.field_of_view = self.field_of_view_
		exploration_goal.starting_position = self.starting_position_
		exploration_goal.planning_mode = self.planning_mode_
		exploration_client = actionlib.SimpleActionClient(self.service_str, RoomExplorationAction)
		self.printMsg("Running room exploration action...")
		self.exploration_result = self.runAction(exploration_client, exploration_goal)
		self.printMsg("Exploration path received with length " + str(len(self.exploration_result.coverage_path_pose_stamped)))
		self.printMsg("Room exploration action completed.")