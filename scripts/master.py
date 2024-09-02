import scripts.partials.cleanup as _cleanup
import scripts.partials.build as _build
import traceback

try:
    
    _build.run()
    _cleanup.run()

except Exception as e:
    # Log the error
    with open('scripts/logs/error.log', 'a') as f:
        f.write(f"An error occurred: {str(e)}\n")
        traceback.print_exc(file=f)

    # Display the error in the console print window
    print(f"An error occurred: {str(e)}")