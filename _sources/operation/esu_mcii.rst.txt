******************************************
ESU Mobile Control 2/Pro
******************************************

.. meta::
   :keywords: ESU MobileControl MC2 MCII Pro

.. include:: ../include.rst

----

.. sidebar::
   :class: sidebar-on-this-page

   .. contents:: On This Page
      :local:
      :depth: 3

.. image:: ../_static/images/gamepads/esu_mcii.png
   :scale: 25 %
   :align: left

As the **ESU Mobile Control 2** and **Mobile Control** Pro are built on an Android platform, and they have made the API available to external developers, |ed| can run on it and make use of the hardware knob and buttons.  Download it from the `Google Play Store <https://play.google.com/store/apps/details?id=jmri.enginedriver>`_ or by :ref:`direct download <downloads/index:older or other versions - manual install>` as you would any other app.

.. warning::
  
    The **ESU Mobile Control 2** does not have a Google Play Services installed, so you will not be able to use the Google Play Store to install |ed|. You will need to :ref:`download the APK file <downloads/index:older or other versions - manual install>` and install it manually.

.. warning::
  
    The **ESU Mobile Control Pro** is currently being shipped with a version of |ED| pre-installed that is *not** compatible with its hardware.  It is also impossible to update the app on the device by downloading an :ref:`APK from this site <downloads/index:older or other versions - manual install>`.  We hope this will be addressed soon, but in the meantime there are some `instructions below <Updating Engine Driver on the ESU Mobile Control Pro>`_ on how to update the app on the device.

Operation
==========

As well as being able to control speed of the selected throttle with the control knob, it's also possible to switch direction via the zero-position end-stop switch.

Up to three trains can be controlled at once - the train being operated by the control knob is highlighted by the small 'v' in the speed indicator. Switch between operated trains by clicking the appropriate speed indicator. It is also possible to assign one of the device side
buttons to switch to the next operated train - by default, the bottom-right button is assigned to this function.

When assigned to control a train, the Green LED is lit. When no trains are assigned, the Green LED flashes.
In addition, you can use the Stop button to pause the currently operated train, or to stop all controlled trains. A short press of the Stop button (default, less than 1/2 second) pauses operation of the currently controlled train. The Red LED will flash quickly to denote this. On a second press of the Stop button, the currently operated train will resume at the previous set speed. A long press of the Stop button (default, greater than 1/2 second) will stop all controlled trains. The Red LED will flash slowly to denote this. On a second press of the Stop button, all controlled trains will remain stationary and it will be possible to again control the currently selected train.

Whilst in stop mode, the on-screen speed change buttons and bar are disabled for currently stopped throttles. Switching between controlled throttles is also disabled. 

Configuration
=============

Default configuration
---------------------

It is possible to configure the device side buttons to perform various actions. The default assignment is as follows:

  Top-left
    Increase speed
  Bottom-left
    Decrease speed
  Top-right
    Toggle direction
  Bottom-right
    Select next throttle

These assignments can be modified via the ESU Mobile Control 2 Options page in Preferences.
 
Recommended Configuration
-------------------------

During the setup wizard for the **ESU Mobile Control 2/Pro**, it will ask if you wish to use the recommended settings for the ESU Mobile Control 2/Pro.  If you select this option, it will set the following configuration:

  Throttle layout
    Horizontal
  Number of Throttle 
    2
  Speed Sliders
    Hidden
  Speed Buttons
    Hidden

Other Configuration
-------------------

You can also configure the physical slider on the **ESU Mobile Control Pro** to perform various actions. 

The Options are currently
  * none
  * 3 Decoder Brake Levels
  * Screen Brightness
  * Use Semi-Realistic Throttle setting 

If the ``3 Decoder Brake Levels`` option is selected, the slider will control the brake level of the currently operated train, using the brake functions of the decoder. This functions exactly like the brake slide in the Semi-Realistic Throttle setting, but it will only work with decoders that support the brake functions.

See the :ref:`operation/semi-realistic-throttle:decoder brake type` for more information on how the the Semi-Realistic Throttle settings work.  This works exactly the same way, but for all throttle layouts, except the Semi-Realistic Throttle layout.

If the ``Use Semi-Realistic Throttle setting`` option is selected, the physical slider will follow whatever :ref:`settings <operation/semi-realistic-throttle:decoder brake type>` you have for the brake slider in the Semi-Realistic Throttle. It will work with any decoder, even if the decoder does not have brake functions.

.. note::
  :class: note-ed-hidden-title

  The setting for the Decoder Brake Functions for the physical slider and the Semi-Realistic Throttle setting are independent of each other.

----

Updating Engine Driver on the ESU Mobile Control Pro
====================================================

The ESU Mobile Control Pro is currently being shipped with a version of |ED| pre-installed that is not compatible with its hardware.  It is also impossible to update the app on the device by downloading an APK from this site.  

These instructions will allow you to update the app on the device from one of the APKs on this website.  Note that currently only the ``EngineDriver-2.40.200a.apk (Alpha)``, or later, is compatible with the **ESU Mobile Control Pro**.

1. You need to download a copy of ``adb.exe``    (e.g. https://developer.android.com/tools/releases/platform-tools )

2. Then open a terminal (``cmd`` or ``powershell``) and navigate to the directory where adb.exe is located. 

    For example, if you have adb.exe in C:\adb, then you would type:
    
    .. code-block::
  
      cd C:\adb
  
3. Open an ``adb`` connection to the device. 
   You will need to enable USB debugging on the device, and connect it to your computer via USB. 

   Type:

  .. code-block::

     adb shell

4. Then Enter these commands line by line: 

  .. code-block::

    $ mount -o remount,rw /
    $ rm -rf /system/app/EngineDriver/
    $ rm -f /data/dalvik-cache/arm/*Engine*
    $ mount -o remount,ro /
    $ pm uninstall --user 0 jmri.enginedriver
    $ reboot

    (You can copy and paste these commands into the terminal window, but make sure you press ``Enter`` after each line.)

5. After the device has rebooted, you can install a new APK from this website.

  * Open the Chrome browser on the MC Pro
  * Navigate to the Engine Driver downloads page: https://www.jmri.org/downloads
  * click the .APK you wish to download