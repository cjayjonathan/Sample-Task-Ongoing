#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install python-telegram-bot')


# In[3]:


from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters


# In[4]:


updater = Updater("5212182556:AAGcP-HYMRMgmo7Fkdf7rFuLqzVrU7sssQM",
				use_context=True)


def start(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Data Science Nuggets Bot Here for You")


# In[5]:


def help(update: Update, context: CallbackContext):
	update.message.reply_text("I am your Butler")


# In[7]:


def naukri_url(update: Update, context: CallbackContext):
	update.message.reply_text("https://www.naukri.com/data-scientist-jobs-in-india")


def linkedIn_url(update: Update, context: CallbackContext):
	update.message.reply_text("https://www.linkedin.com/jobs/search/?keywords=data%20scientist")


def glassdoor_url(update: Update, context: CallbackContext):
	update.message.reply_text("https://www.glassdoor.co.in/Job/india-data-scientist-jobs-SRCH_IL.0,5_IN115_KO6,20.htm")

def datasciencenuggets_url(update: Update, context: CallbackContext):
	update.message.reply_text("https://nuggetsnetwork.com/blog/Data-Science-Jobs-In-India.html")


def unknown_text(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry I can't recognize you , you said '%s'" % update.message.text)


def unknown(update: Update, context: CallbackContext):
	update.message.reply_text(
		"Sorry '%s' is not a valid command" % update.message.text)


# In[8]:


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('naukri', naukri_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('glassdoor', glassdoor_url))
updater.dispatcher.add_handler(CommandHandler('datasciencenuggets', datasciencenuggets_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
	# Filters out unknown commands
	Filters.command, unknown))

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))


# In[10]:


updater.start_polling()


# In[ ]:




