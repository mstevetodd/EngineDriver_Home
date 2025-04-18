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

If |ED| says that you are not connected to a network on the Connection screen, check that `Use Location` is enabled.

Incompatible Routers
^^^^^^^^^^^^^^^^^^^^^

While uncommon, one reason why your |SERVER| may not be visible in the Discovered list on the connection screen can be that your router or network does not support the Bonjour/mDNS protocol. 

In this case, enter the server address and port manually, or select it from Recents.

Firewalls
---------

.. todo:: 
  :class: todo-float-right
  
  LOW: Firewalls

Your PC's firewall software can prevent |ed| from connecting to your |SERVER|. 

You may need to add an exception in your firewall software for the incoming port or disable the firewall to allow |ed| to connect.

Routers and Mesh networks
-------------------------

2.4GHz and 5GHz
^^^^^^^^^^^^^^^

Some routers do not transfer the mDNS messages between clients on the 2.4GHz and 5ghz channels.  So if your |SERVER| is using 2.4GHz, make sure your device/phone is using a 2.4GHz channel as well. (Or both use 5GHz channels.)

The |EX-CS| uses 2.4GHz WiFi only.  So if you are using one of these devices, make sure your device/phone is using a 2.4GHz channel as well.

Mesh Routers
^^^^^^^^^^^^

Many Mesh routers will not transfer the mDNS messages to other connected routers / modems. 

If you are using a mesh network, either:

* enter the server address and port manually, or select it from Recents
* make sure both the |SERVER| and the device/phone are using the same Mesh network, or

Using Mobile Data instead of WiFi
---------------------------------

Recent versions of Android have a very confusing *feature*, sometimes called 'Smart Network Switching', that will ignore a connected WiFi network if that network cannot reach the Internet. 

This can cause problems if you sometimes use your device to connect to the internet on one network, but your |WTS-DCC-EX| is on a different network that does not have an internet connection. 

Sometimes, the network can show as connected, and EngineDriver server discovery works, but clicking on the discovered server or Connect button does not work.

Some devices have a setting to turn off this feature, some do not. 

Some provide a notification that "Wi-Fi has no internet access, Tap for options", followed by "This network has no internet access. Stay connected?" that can be used to disable this feature and remain connected to the WiFi. 

If you missed the prompt, you can 'forget' the network, and re-enter your WiFi credentials to get the prompt again.

Workaround: If you are unable to turn off the feature, you can enable ``Airplane Mode``, then enable ONLY WiFi, and then connect your WiFi.

.. important:: 

  Recent versions of |ED| now try to handle this *feature* by "forcing" the local WiFi connection.  
  
  |ED| will show a message "Using MOBILE network, not WiFi. check WiFi settings", when this mode is encountered.

  There is an :ref:`Allow Mobile Data Connection <configuration/preferences:mobile data connection?>` preference that can be enabled if you need to force |ED| to access the mobile data.  (rarely needed)

Disconnections
--------------

|ed| and/or the Android device can occasionally lose the connection even after it successfully connected.  

There can be a lot of causes.  If ED does lose connection it will buzz, vibrate and take you to *Reconnecting Screen*.   It will repeatedly and indefinitely attempt to reconnect.

Some possible causes include:

* `Other networks on the same channel`_
* `Distance to router / location of the router`_
* `Too Many Devices Are Connected`_
* `Objects in the way` (particularly metal objects)
* Interference  (Other electrical devices close to the phone or the router )

If the |SERVER| does not receive any feedback from your device/phone within a configured period, the |SERVER| should stop all the locos you have selected on your device/phone.

.. note:: 
  :class: note-ed-hidden-title
  
  See `Feedback on Disconnect preference on the Preferences page <../configuration/preferences.html#feedback-on-disconnect>`_ to disable the audible and haptic warnings.

Other networks on the same channel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One problem that can cause disconnections is if there are other, busy, networks on the same channel as your network.  You can use a WiFi analyzer app (e.g. `WiFiAnalyzer (Open Source) <https://play.google.com/store/apps/details?id=com.vrem.wifianalyzer&hl=en_AU>`_` ) to see what channels are being used by other networks and change your network to a less used channel.  If your router (or Wifi CommandStation) is on a busy channel, try moving it to a less busy channel.

Distance to router / location of the router
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

One problem that can cause disconnections is if there you are too far from you router.  You can use a WiFi analyzer app (e.g. `WiFiAnalyzer (Open Source) <https://play.google.com/store/apps/details?id=com.vrem.wifianalyzer&hl=en_AU>`_` ) to see what signal strength you have as your move around you layout.  If you are too far from the router, you may need to move the router closer to the layout, or add a WiFi extender.

Objects in the way
^^^^^^^^^^^^^^^^^^

One problem that can cause disconnections is if there are objects in the way (particularly metal objects) in the part to your router. So it may be fine at one loaction, but not at another. You can use a WiFi analyzer app (e.g. `WiFiAnalyzer (Open Source) <https://play.google.com/store/apps/details?id=com.vrem.wifianalyzer&hl=en_AU>`_` ) to see what signal strength you have as you move around your layout.  If you are find it drops at certain loacations, you may need to move the router closer to the layout, or add a WiFi extender.

Too Many Devices Are Connected
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Most Wifi Command Stations support only a small number connectred devices/phones.  e.g. **LnWi** and the DIY version of the |EX-CS| only support 4 connections. The prebuilt |DCC-EX| EX-CSB1 supports 10 connections.

When you try to connect to a |SERVER| that has reached its maximum number of connections, the results can be unpredictable.  You may be able to connect, but then get disconnected, you may not be able to connect at all, or you may connect but someone else will get disconnected.

|JMRI| does not have this limitaion.  It will accept as many connections as the Wifi Router can handle.
