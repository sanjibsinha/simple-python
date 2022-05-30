class DesktopLamp:
    is_off = "off"
    is_on = "on"
    
    def switch_on(self, is_on):
        print(f"The lamp is {is_on}")
        
    def switch_off(self, is_off):
        print(f"The lamp is {is_off}")

def main():
      lamp = DesktopLamp()
      lamp.switch_on("switched on")
      # The lamp is switched on
      lamp.switch_off("switched off")
      # The lamp is switched off
      
if __name__ == '__main__': main()