function find_botty {
  echo "Finding Botty process..."
  BOTTYPID=$(pgrep -f "python3 -u brains.py")
  export BOTTYPID
}

function stop_botty {
  find_botty
  if [ ! -z "$BOTTYPID" ]; then
    echo "Found Botty process @PID: $BOTTYPID"
    echo "Killing botty process..."
    kill ${BOTTYPID}
  else
        echo "No Botty process found"
  fi
}

function start_botty {
  echo "Starting Botty Process..."
  python3 -u brains.py > /dev/null &
  find_botty
  if [ ! -z "$BOTTYPID" ]; then
    echo "Found Botty process @PID: $BOTTYPID"
  else
    echo "No Botty process found"
  fi
}

if [ ! -z "$1" ]; then
  ARGUMENT=$1
  echo "Going to $ARGUMENT Botty"
  if [[ "$ARGUMENT" == "stop" || "$ARGUMENT" == "bounce" ]]; then
    stop_botty
  fi

  if [[ "$ARGUMENT" == "start" || "$ARGUMENT" == "bounce" ]]; then
    start_botty
  fi

else
  echo "Missing a script argument [start, stop, bounce]"
fi
