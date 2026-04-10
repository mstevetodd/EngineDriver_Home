:orphan:

*************************************************************************************
Programming on the Main (PoM)
*************************************************************************************

.. meta::
   :keywords: CV Programming Main POM

.. include:: ../include.rst

.. sidebar::
   :class: sidebar-on-this-page

   .. contents:: On This Page
      :local:
      :depth: 3

The |NATIVE| allows |ED| to read and write CVs of decoders on both the Main on a Prog tracks. The |NATIVE| is only available when connected to a |EX-CS| and is discussed on the :doc:`/operation/dcc-ex-native-protocol` page.

The |WIT|, which is used for connecting to Command Stations other that the |EX-CS|, does not provide for any CV programming.

However it is possible to use a feature implemented in some system to do programming on the main (PoM) to write to CVs (not read).

.. important:: 

  This feature only works on a very small number of DCC Command Stations.  It works by sending a hex packet to the DCC Command Station.

To use this feature, enable the :ref:`configuration/preferences:Show WiThrottle PoM Page` preference.


Write CVs of decoders on the Main Track
---------------------------------------

.. image:: ../_static/images/screenshots/pom_screen.png
   :scale: 8 %
   :align: right

Note that you cannot read CVs or DCC Addresses on the main track.  You can only write CVs of a specified loco (DCC Address).

To write a new CV value, enter the DCC address of the loco you want to change, enter the CV number into the 'CV' field, enter the new value in the 'Value' field and press :guilabel:`Write`

Optionally, you can use the :guilabel:`NRMA CVs` pulldown to select a common CV from a list.  This just enters the appropriate CV number in the 'CV' field.

|FORCE-BREAK|