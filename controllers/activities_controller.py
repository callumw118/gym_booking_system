from flask import Blueprint, Flask, redirect, render_template, request

from models.activity import Activity
import repositories.activity_repository as activity_repository

activities_blueprint = Blueprint("activities", __name__)

