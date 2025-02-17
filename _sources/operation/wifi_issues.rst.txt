*******************************************
WiFi Issues
*******************************************

.. meta::
   :keywords: WiFi 

.. include:: ../include.rst

----

.. sidebar::
   :class: sidebar-on-this-page

   .. contents:: On This Page
     :local:

Many of the problems that people have with |ed| relate to connection issues.

Below are several common problems.

Bonjour/mDNS
-------------

Use location
^^^^^^^^^^^^

The Android System setting `Use Location` must be enabled for |ED| to be able to discover servers.

If |ED| says that you are not connected to a network on the Connection screen, check the `Use Location` is enabled.

Incompatible Routers
^^^^^^^^^^^^^^^^^^^^^

While very uncommon, one reason why your |SERVER| may not be visible in the discovered list on the connection screen can be that your router doesn't not support the Bonjour/mDNS protocol. There is not much you can do if this is the case other than trying a different router.

Firewalls
---------

.. todo:: 
  :class: todo-float-right
  
  LOW: Firewalls

Your PC's firewall software can prevent |ed| from connecting to JMRI. You may need to add an exception in your firewall software for JMRI or disable the firewall to allow |ed| to connect.

Routers and Mesh networks
-------------------------

4.5ghz and 5ghz
^^^^^^^^^^^^^^^

Some routers do not transfer the mDNS messages between clients on the 4.5ghz and 5ghz channels.  So if your |SERVER| is using 4.5ghz, make sure you device/phone is using a 4.5ghz channel as well. (Or both use 5ghz channels.)

Mesh Routers
^^^^^^^^^^^^

Many Mesh routers will not transfer the mDNS messages to other connected routers / modems. If you are using a mesh network, make sure both the |SERVER| and the device/phone are using the same Mesh network.

Using Mobile Data instead of WiFi
---------------------------------

Recent versions of Android have a very confusing *feature*, sometimes called 'Smart Network Switching', that will ignore a connected WiFi network if that network cannot reach the Internet. 

This can cause problems if you sometimes use your device to connect to the internet on one network, but your |WTS-DCC-EX| is on a different network that does not have an internet connection. 

Sometimes, the network can show as connected, and EngineDriver server discovery works, but clicking on the discovered server or Connect button does not work.

As of |ED| version 2.26.115, |ED| now handles this situation by "forcing" the local WiFi connection.  There is an :ref:`Allow Mobile Data Connection <configuration/preferences:mobile data connection?>` preference that can be enabled if needed.

EngineDriver will show a message "Using MOBILE network, not WiFi. check WiFi settings", when this mode is encountered.

Some devices have a setting to turn off this feature, some do not. 

Some provide a notification that "Wi-Fi has no internet access, Tap for options", followed by "This network has no internet access. Stay connected?" that can be used to disable this feature and remain connected to the WiFi. 

If you missed the prompt, you can 'forget' the network, and re-enter your WiFi credentials to get the prompt again.

Workaround: If you are unable to turn off the feature, you can enable ``Airplane Mode``, then enable ONLY WiFi, and then connect your WiFi.

Disconnections
--------------

.. todo:: 
  :class: todo-float-right
  
  MEDIUM: Disconnections

|ed| and/or the Android device can occasionally lose the connection even after it successfully connected.  There can be a lot of causes.  If ED does lose connection it will buzz, vibrate and take you to *Reconnecting Screen*.   It will repeatedly and indefinitely attempt to reconnect.

* Other networks on the same channel
* distance to router / location of the router
* Too Many Devices Are Connected
* objects in the way (particularly metal objects)
* Interference  (Other electrical devices close to the phone or the router )

If JMRI does not receive any feedback from your device/phone within a configured period, JMRI will stop all the locos you have selected on your device/phone.

* Disable haptic Alert


.. note:: 
  :class: note-ed-hidden-title
  
  See `Feedback on Disconnect preference on the Preferences page <../configuration/preferences.html#feedback-on-disconnect>`_ to disable the audible and haptic warnings.
