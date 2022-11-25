package com.liudonghua.examples;

import java.io.BufferedInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;

import javax.sound.midi.MidiSystem;
import javax.sound.midi.Sequencer;

/**
 * MidiPlayer example
 * 
 * source: https://examples.javacodegeeks.com/desktop-java/sound/play-midi-audio/
 * https://docs.oracle.com/javase/8/docs/technotes/guides/sound/
 * https://riptutorial.com/java/example/621/play-a-midi-file
 */
public class App {

    public static void main(String[] args) throws Exception {
        // check whether the input file as cli arguments is specified
        if (args.length < 1) {
            System.out.println("Usage: ./app <midifile>");
            System.exit(0);
        }
        // Obtains the default Sequencer connected to a default device.
        Sequencer sequencer = MidiSystem.getSequencer();
        // Opens the device, indicating that it should now acquire any
        // system resources it requires and become operational.
        sequencer.open();
        // create a stream from a file
        InputStream is = new BufferedInputStream(new FileInputStream(new File(args[0])));
        // Sets the current sequence on which the sequencer operates.
        // The stream must point to MIDI file data.
        sequencer.setSequence(is);
        // Starts playback of the MIDI data in the currently loaded sequence.
        sequencer.start();
    }

}