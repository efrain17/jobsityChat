"""This module manage conection model"""
from libraries import hooks
from controllers import conection as conection_ctr


@hooks.session_committer
def insert_conection(event, unused_context):
	"""Insert new conection"""
	conection_ctr.insert_conection(event)
	return 'success'


@hooks.session_committer
def delete_conection(event, unused_context):
	"""Insert new conection"""
	conection_ctr.delete_conection(event)
	return 'success'
