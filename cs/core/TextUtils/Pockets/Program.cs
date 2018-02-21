using System;

namespace Pockets
{
    public class UnitConverter
    {
        int ratio;

        public UnitConverter(int unitRatio)
        {
            this.ratio = unitRatio;
        }

        public int Convert(int unit)
        {
            return unit * ratio;
        }

        static void Main(string[] args)
        {
            var feetToInches = new UnitConverter(12);
            var milesToFeet = new UnitConverter(5280);

            Console.WriteLine(feetToInches.Convert(30));
            Console.WriteLine(feetToInches.Convert(100));
            Console.WriteLine(feetToInches.Convert(milesToFeet.Convert(1)));
        }
    }
}
