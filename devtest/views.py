import subprocess
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from devtest.forms import DeviceTestForm
from django.contrib import messages
from devtest.models import Device

def home(request):
    return render(request, 'home.html')

def device_test(request):
    result = None
    form = DeviceTestForm(request.POST or None)  # Initialize the form based on the request

    if request.method == "POST" and form.is_valid():
        device = form.cleaned_data['device']
        result = run_ipperf_test(device.name)

    return render(request, 'device_test.html', {'form': form, 'result': result})

def run_ipperf_test(device_name):
    # Command to run iperf test
    command = ['iperf', '-c', device_name]  # Using a list for the command
    try:
        output = subprocess.check_output(command, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Error: {e.output}"  # Return the error output for debugging
