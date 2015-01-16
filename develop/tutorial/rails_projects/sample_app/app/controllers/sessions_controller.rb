class SessionsController < ApplicationController
  protect_from_forgery  with: :exception
  include SessionsHelper

  def new
  	render 'new'
  end

  def create
  	email = params[:session][:email].downcase
  	password = params[:session][:password]
  	user = User.find_by(email: email)
  	if user && user.authenticate(password)
  		log_in user
      params[:session][:remember_me] == "1"? remember(user) : forget(user)
  		redirect_to user_url(user)
  	else
  		flash.now[:danger] = "Invalid email/password combination"
  		render 'new'
  	end
  end

  def destroy
  	log_out
  	redirect_to root_url
  end

end
